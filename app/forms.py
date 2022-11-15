from django import forms
from .models import News, Images


# NEWSLATTER
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

# IMAGES
class ImagesForm(forms.ModelForm):

    titulo = forms.CharField(
        min_length=3,
        max_length=50,
        widget=forms.TextInput(attrs= {
            'style':'font-size: 13px',
            'placeholde':'Dê um título'
        })
    )

    class Meta:
        model = Images
        fields = '__all__'

    # Super Function
    def __init__(self, *args, **kwargs):
        super(ImagesForm, self).__init__(*args, **kwargs)
        # (Reduzir a repetição de codigo, Via Array)
        slide = ['img_01', 'img_02', 'img_03', 'img_04', 'img_05', 'img_06']
        for img in slide:
            self.fields[img].widget = forms.FileInput()
            self.fields[img].label = ''
            self.fields[img].widget.attrs.update(
                {
                    'style': 'font-size: 13px',
                    'accept': 'image/png, image/jpeg',
                    'class': 'form-control-sm'
                }
            )

