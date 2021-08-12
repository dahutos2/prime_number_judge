from django import forms
from django.core.exceptions import ValidationError

widget_textinput = forms.TextInput(
    attrs={
        "class": "form-control"
    }
)


class TextForm(forms.Form):
    a = forms.FloatField(label='10000円',widget=widget_textinput)
    b = forms.FloatField(label='5000円',widget=widget_textinput)
    c = forms.FloatField(label='1000円',widget=widget_textinput)
    d = forms.FloatField(label='500円',widget=widget_textinput)
    e = forms.FloatField(label='100円',widget=widget_textinput)
    f = forms.FloatField(label='50円',widget=widget_textinput)
    g = forms.FloatField(label='10円',widget=widget_textinput)
    h = forms.FloatField(label='5円',widget=widget_textinput)
    i= forms.FloatField(label='1円',widget=widget_textinput)
    j = forms.FloatField(label='500棒',widget=widget_textinput)
    k = forms.FloatField(label='100棒',widget=widget_textinput)
    l = forms.FloatField(label='50棒',widget=widget_textinput)
    m = forms.FloatField(label='10棒',widget=widget_textinput)
    n = forms.FloatField(label='5棒',widget=widget_textinput)
    o = forms.FloatField(label='1棒',widget=widget_textinput)
    
    def clean(self):
        # djangoもともとのバリデーションを実行してデータを取得
        data = super().clean()
        if not len(data) == 15:
            raise ValidationError("数字を入力してください")
        
        return data
