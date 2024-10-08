from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Ticket
from .forms import TicketForm

# Dashboard showing all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

# View for tickets within a specific project
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    tickets = project.tickets.all()  # Access related tickets
    return render(request, 'project_detail.html', {'project': project, 'tickets': tickets})

# Create ticket for a specific project
def ticket_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.project = project  # Link the ticket to the project
            ticket.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = TicketForm()
    return render(request, 'ticket_form.html', {'form': form, 'project': project})

# Ticket detail view
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket_detail.html', {'ticket': ticket})

# Update ticket status
def ticket_update_status(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get('status')
        if new_status in dict(Ticket.STATUS_CHOICES).keys():
            ticket.status = new_status
            ticket.save()
        return redirect('ticket_detail', pk=ticket.pk)
    return render(request, 'ticket_update_status.html', {'ticket': ticket})
