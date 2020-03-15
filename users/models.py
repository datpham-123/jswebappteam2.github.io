from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# delete user -> delete profile: delete profile -> not delete user
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    fullname=models.CharField(max_length=100, default = 'Wu an  Rose')
    dob = models.DateField(null = True, blank = True)
    studentID=models.CharField(max_length = 12, default='HE1xxxx')
    role = models.CharField(max_length=30, default='Ban chuyên môn')
    bio = models.CharField(max_length=100, default ='Cần cù thì bù siêng năng-Có làm thì mới có ăn')
    address = models.CharField(max_length = 30, default='Hà Nội')
    phone = models.CharField(max_length = 12, default='09x-xxxxxxx')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 325 or img.width >325:
            output_size = (325,325)
            img.thumbnail(output_size)
            img.save(self.image.path)

# 15:24 (1): start extends user models here: 3/11
