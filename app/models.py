from django.db import models

# Newsletter

class News(models.Model):
    email = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = 'Inscritos no site'


# Countdown
class Timer(models.Model):
    id = models.IntegerField(primary_key=True)
    timer = models.CharField(max_length=100, blank=True)
    class Meta:
        verbose_name_plural = 'Contagem Regressiva'


# Typed Effect
class Typed(models.Model):
    id = models.IntegerField(primary_key=True)
    fixo = models.CharField(max_length=50)
    txt_01 = models.CharField(max_length=50)
    txt_02 = models.CharField(max_length=50)
    txt_03 = models.CharField(max_length=50)
    txt_04 = models.CharField(max_length=50)
    def __str__(self):
        return self.fixo
    class Meta:
        verbose_name_plural = 'Efeito de digitação'

# Music
class Music(models.Model):
    id = models.IntegerField(primary_key=True)
    title_music = models.CharField(max_length=50)
    music = models.FileField()

    def __str__(self):
        return self.title_music
    class Meta:
        verbose_name_plural = 'Musica de fundo'

# Slide Images
class Images(models.Model):
    titulo = models.CharField(max_length=50)
    img_01 = models.ImageField(blank=True)
    img_02 = models.ImageField(blank=True)
    img_03 = models.ImageField(blank=True)
    img_04 = models.ImageField(blank=True)
    img_05 = models.ImageField(blank=True)
    img_06 = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = 'Slide de Imagens'

# Default Image
class Default(models.Model):
    titulo = models.CharField(max_length=50)
    img_default = models.ImageField(blank=True)
    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name_plural = 'Imagem padrão'


# Home Editavel
class Home(models.Model):
    id = models.IntegerField(primary_key=True)
    # Titulo
    home_title = models.CharField(max_length=50)
    icon_title = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    # Card 1 (verde)
    card_title01 = models.CharField(max_length=50)
    card_color01 = models.CharField(max_length=50)
    card_icon01 = models.CharField(max_length=50)
    txt_card_a1 = models.CharField(max_length=50)
    txt_card_b1 = models.CharField(max_length=50)
    txt_card_c1 = models.CharField(max_length=50)
    # Card 2 (Vermelho)
    card_title02 = models.CharField(max_length=50)
    card_color02 = models.CharField(max_length=50)
    card_icon02 = models.CharField(max_length=50)
    txt_card_a2 = models.CharField(max_length=50)
    txt_card_b2 = models.CharField(max_length=50)
    txt_card_c2 = models.CharField(max_length=50)

    btn_color = models.CharField(max_length=50)
    icon_type = models.CharField(max_length=50)

    # Modal
    modal_title = models.CharField(max_length=50)
    modal_card_title = models.CharField(max_length=50)
    modal_card_color = models.CharField(max_length=50)
    modal_card_icon = models.CharField(max_length=50)
    cargo01 = models.CharField(max_length=50)
    cargo02 = models.CharField(max_length=50)
    cargo03 = models.CharField(max_length=50)
    cargo04 = models.CharField(max_length=50)
    cargo05 = models.CharField(max_length=50)

    def __str__(self):
        return self.home_title
    class Meta:
        verbose_name_plural = "Textos da HomePage"
