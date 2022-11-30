from django import forms

class AccommodationReviewForm(forms.Form):

    score_attrs = {
        'type':'number',
        'name':'score',
        'id':'score',
        'min': '0',
        'max': '5'
    }

    score = forms.IntegerField(min_value=0, label='', required=True, 
        widget=forms.NumberInput(attrs=score_attrs))

    comment_attrs = {
        'type':'text',
        'name':'comment',
        'id': 'comment',
        'placeholder':'Write your comment here..'
    }

    comment = forms.CharField(label="",required=True,
        widget=forms.Textarea(attrs=comment_attrs))
