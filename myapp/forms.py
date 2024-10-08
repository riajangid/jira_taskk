from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'assigned_to']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Customizing the description field
            'assigned_to': forms.TextInput(attrs={'placeholder': 'Assignee Name'})  # Placeholder for assigned_to
        }

    def clean_assigned_to(self):
        assigned_to = self.cleaned_data.get('assigned_to')
        if assigned_to and len(assigned_to) < 3:
            raise forms.ValidationError("Assignee name must be at least 3 characters long.")
        return assigned_to
