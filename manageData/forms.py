from django import forms
from django import views

class DestinationAreaForm(forms.Form):
    province_attrs = {
        'type' : 'text',
        'name' : 'province',
        'id' : 'province',
        'placeholder' : 'Enter the province HERE'
    }
    province = forms.CharField(label="", required=True, widget=forms.TextInput(attrs=province_attrs))

    city_attrs = {
        'type' : 'text',
        'name' : 'city',
        'id' : 'city',
        'placeholder' : 'Enter the city HERE'
    }
    city = forms.CharField(label="", required=True, widget=forms.TextInput(attrs=city_attrs))

    desc_attrs = {
        'type' : 'text',
        'name' : 'desc',
        'id' : 'desc',
        'placeholder' : 'Description...'
    }
    desc = forms.CharField(label="", required=False, widget=forms.Textarea(attrs=desc_attrs))

    pic_attrs = {
        'type' : 'text',
        'name' : 'pic',
        'id' : 'pic',
        'placeholder' : 'Enter picture link HERE'
    }
    pic = forms.CharField(label="", required=False, widget=forms.TextInput(attrs=pic_attrs))

class SiteForm(forms.Form):
    def __init__(self, item_list, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.list_choices = [(x[0],  ', '.join(x[1:])) for x in item_list]
        self.fields['dest_area'] = forms.ChoiceField(choices=self.list_choices)
    dest_area = forms.ChoiceField()

    name_attrs = {
        'type' : 'text',
        'name' : 'name',
        'id' : 'name',
        'placeholder' : 'Enter site name HERE'
    }
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs=name_attrs))

    desc_attrs = {
        'type' : 'text',
        'name' : 'desc',
        'id' : 'desc',
        'placeholder' : 'Description...'
    }
    desc = forms.CharField(label="", required=False, widget=forms.Textarea(attrs=desc_attrs))

    pic_attrs = {
        'type' : 'text',
        'name' : 'pic',
        'id' : 'pic',
        'placeholder' : 'Enter picture link HERE'
    }
    pic = forms.CharField(label="", required=False, widget=forms.TextInput(attrs=pic_attrs))

class AccommodationForm(forms.Form):
    def __init__(self, item_list, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.list_choices = [(x[0],  ', '.join(x[1:])) for x in item_list]
        self.fields['dest_area'] = forms.ChoiceField(choices=self.list_choices)
    dest_area = forms.ChoiceField()

    name_attrs = {
        'type' : 'text',
        'name' : 'name',
        'id' : 'name',
        'placeholder' : 'Enter accommodation name HERE'
    }
    name = forms.CharField(label="", required=True, widget=forms.TextInput(attrs=name_attrs))

    desc_attrs = {
        'type' : 'text',
        'name' : 'desc',
        'id' : 'desc',
        'placeholder' : 'Description...'
    }
    desc = forms.CharField(label="", required=False, widget=forms.Textarea(attrs=desc_attrs))

    pic_attrs = {
        'type' : 'text',
        'name' : 'pic',
        'id' : 'pic',
        'placeholder' : 'Enter picture link HERE'
    }
    pic = forms.CharField(label="", required=False, widget=forms.TextInput(attrs=pic_attrs))
    
    price_attrs = {
        'type' : 'number',
        'name' : 'price',
        'id' : 'price',
        'min': '0',
        'placeholder' : 'Enter price HERE'
    }
    price = forms.IntegerField(min_value=0, label="", required=True, widget=forms.NumberInput(attrs=price_attrs))