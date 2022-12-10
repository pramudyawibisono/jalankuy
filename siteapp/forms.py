from django import forms

class SiteReviewForm(forms.Form):

    score_attrs = {
        'type':'number',
        'class': 'form-control',
        'name':'score',
        'id':'score',
        'min': '0',
        'max': '5'
    }

    score = forms.IntegerField(min_value=0, label='', required=True, 
        widget=forms.NumberInput(attrs=score_attrs))

    comment_attrs = {
        'type':'text',
        'class': 'form-control',
        'name':'comment',
        'id': 'comment',
        'rows': '7',
        'placeholder':'Write your review here...'
    }

    comment = forms.CharField(label="",required=True,
        widget=forms.Textarea(attrs=comment_attrs))