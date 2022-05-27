from django import forms
from notesapp.models import Note


class NoteCreateForm(forms.ModelForm):
    tag = forms.CharField(max_length=100)

    class Meta:
        model = Note
        fields = ['title', 'content', 'tag']

    def save(self, commit=True, **kwargs):
        form = super(NoteCreateForm, self).save(commit=False)
        tags = list(self.cleaned_data['tag'].split(','))

        if commit:
            form.save()
            for tag in tags:
                Note.objects.create(tags=tag, note=form)
        return form