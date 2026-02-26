from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Member
from .utils import generate_id_card


@receiver(post_save, sender=Member)
def create_member_id_card(sender, instance, created, **kwargs):
	if created and not instance.id_card:
		file_path = generate_id_card(instance)
		instance.id_card = file_path 
		instance.save() 

#Member.objects.filter(pk=isinstance.pk).update(id_card=file_path)