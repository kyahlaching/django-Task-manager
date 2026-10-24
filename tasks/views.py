
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")

    status = request.GET.get("status")
    if status in ["Pending", "In Progress", "Completed"]:
        tasks = tasks.filter(status=status)

    return render(
        request,
        "tasks/task_list.html",
        {
            "tasks": tasks,
            "selected_status": status or "",
            "today": timezone.localdate(),
        },
    )


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "tasks/task_detail.html", {"task": task})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm()

    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "page_title": "Create Task"},
    )


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_detail", pk=task.pk)
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "page_title": "Edit Task"},
    )


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("task_list")

    return render(
        request,
        "tasks/task_confirm_delete.html",
        {"task": task},
    )
