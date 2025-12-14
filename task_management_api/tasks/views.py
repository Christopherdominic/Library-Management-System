from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwner

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        status_param = self.request.query_params.get('status')
        priority = self.request.query_params.get('priority')
        due_date = self.request.query_params.get('due_date')
        ordering = self.request.query_params.get('ordering')

        if status_param:
            queryset = queryset.filter(status=status_param.upper())
        if priority:
            queryset = queryset.filter(priority=priority.upper())
        if due_date:
            queryset = queryset.filter(due_date=due_date)
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status == 'COMPLETED':
            return Response(
                {"error": "Completed task cannot be edited"},
                status=400
            )
        return super().update(request, *args, **kwargs)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'COMPLETED'
        task.completed_at = timezone.now()
        task.save()
        return Response({"message": "Task marked as completed"})

    @action(detail=True, methods=['post'])
    def reopen(self, request, pk=None):
        task = self.get_object()
        task.status = 'PENDING'
        task.completed_at = None
        task.save()
        return Response({"message": "Task reopened"})

