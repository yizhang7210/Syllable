from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
import re

class Grip(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    deleted = models.BooleanField(default=False)
    created_by = models.EmailField(db_index=True) # No cross app reference
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' by ' + str(self.created_by)

def get_by_creator(creator_email):
    return Grip.objects.filter(
        created_by=creator_email,
        deleted=False).order_by('-created_at')

def get_by_id(id):
    try:
        return Grip.objects.get(id=id)
    except ObjectDoesNotExist:
        return None

def get_by_search(user_email, searchTerm):
    querySet = Grip.objects.filter(created_by=user_email, deleted=False)

    query = process_query(searchTerm)
    querySet = querySet.extra(
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
    return querySet.order_by('-created_at')

def create_one(**kwargs):
    return Grip(**kwargs)

def save(grip):
    grip.save()


# https://www.fusionbox.com/blog/detail/partial-word-search-with-postgres-full-text-search-in-django/632/
def process_query(searchTerm):
    query = re.sub(r'[!\'()|&]', ' ', searchTerm).strip()
    if query:
        query = re.sub(r'\s+', ' & ', query)
        # Support prefix search on the last word. A tsquery of 'toda:*' will
        # match against any words that start with 'toda', which is good for
        # search-as-you-type.
        query += ':*'
    return query
