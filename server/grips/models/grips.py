import re
from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Grip(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    deleted = models.BooleanField(default=False)
    created_by = models.EmailField(db_index=True) # No cross app reference
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owned_by = models.CharField(max_length=50) # user email or org id

    def __str__(self):
        return self.title + ' by ' + str(self.created_by)

def get_by_creator(creator_email):
    return Grip.objects.filter(
        created_by=creator_email,
        deleted=False).order_by('-created_at')

def get_by_owner(owner_identifier):
    return Grip.objects.filter(
        owned_by=owner_identifier,
        deleted=False).order_by('-created_at')

def get_by_id(grip_id):
    try:
        return Grip.objects.get(id=grip_id)
    except ObjectDoesNotExist:
        return None

def search(query_set, search_term):
    query = process_query(search_term)
    query_set = query_set.extra(
        where=[
            '''
            to_tsvector('english', concat_ws(' ',
                title,
                content
            )) @@ to_tsquery('english', %s)
            '''
        ],
        params=[query],
    )
    return query_set.order_by('-created_at')

def create_one(**kwargs):
    return Grip(**kwargs)

def save(grip):
    grip.save()
    return grip


# https://www.fusionbox.com/blog/detail/partial-word-search-with-postgres-full-text-search-in-django/632/
def process_query(search_term):
    query = re.sub(r'[!\'()|&]', ' ', search_term).strip()
    if query:
        query = re.sub(r'\s+', ' & ', query)
        # Support prefix search on the last word. A tsquery of 'toda:*' will
        # match against any words that start with 'toda', which is good for
        # search-as-you-type.
        query += ':*'
    return query
