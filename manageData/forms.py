from django import forms

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
    dest_area_attrs = {
        'type' : 'number',
        'name' : 'dest_area',
        'id' : 'dest_area',
        'min': '1'
    }
    dest_area = forms.IntegerField(min_value=1, label='', required=True, widget=forms.NumberInput(attrs=dest_area_attrs))

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
    dest_area_attrs = {
        'type' : 'number',
        'name' : 'dest_area',
        'id' : 'dest_area',
        'min': '1'
    }
    dest_area = forms.IntegerField(min_value=1, label='', required=True, widget=forms.NumberInput(attrs=dest_area_attrs))

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
    
    price_attrs = {
        'type' : 'number',
        'name' : 'price',
        'id' : 'price',
        'min': '0'
    }
    price = forms.IntegerField(min_value=0, label='', required=True, widget=forms.NumberInput(attrs=price_attrs))