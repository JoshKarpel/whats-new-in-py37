# https://docs.python.org/3.7/library/dataclasses.html

from dataclasses import dataclass, field, asdict, astuple
import datetime


@dataclass
class BlogPost:
    title: str
    body: str
    comments: list = field(default_factory = list)  # comments = [] would be a default mutable argument!
    posted: datetime.datetime = field(default_factory = datetime.datetime.now)

    def line(self, n):
        return self.body.splitlines()[n]

    @property
    def slug(self):
        return self.title.lower().replace(' ', '-').replace('?', '')

    def __len__(self):
        return len(self.body)


post = BlogPost(
    title = "What's New in Python 3.7?",
    body = 'Literally this example.\nThis is the second line.'
)

print(f'STR  => {post}')
print(f'REPR => {repr(post)}')

print()

print(f'AS TUPLE => {astuple(post)}')
print(f'AS DICT  => {asdict(post)}')

print()

print(f'NORMAL METHOD => {post.line(1)}')
print(f'PROPERTY      => {post.slug}')
print(f'DUNDER METHOD => {len(post)}')
