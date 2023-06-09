# See the database app
set FLASK_APP=app
set FLASK_ENV=development
flask shell
from app.extensions import db
print(db)

# Create tables based on the post model:
flask shell
from app.extensions import db
from app.models.auth import Auth
db.create_all()

# Note: The db.create_all() function does not recreate or update a table if it already exists. For example, if you want to modify your model by adding a new column and so you run the db.create_all() function, the change you make to the model will not be applied to the table if the table already exists in the database. The solution is:
db.drop_all()
db.create_all()
# > These commands will apply the modifications you make to your models and will delete all the existing data in the database. To update the database and preserve existing data, you’ll need to use schema migration, which allows you to modify your tables and preserve data. You can use the Flask-Migrate extension to perform SQLAlchemy schema migrations through the Flask command-line interface.

### Command to create ten random posts [flask shell]:
import random

for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    post = Post(title=f'Post #{random_num}',
                content=f'Content #{random_num}')
    db.session.add(post)
    print(post)
    print(post.content)
    print('--')
    db.session.commit()

### Command to create random questions [flask shell]
from app.extensions import db
from app.models.question import Question
db.create_all()

q1 = Question(content='Why is the sky blue?', answer='Because... Why not?')
q2 = Question(content='What is love?', answer='A portal to the underworld.')
db.session.add_all([q1, q2])
db.session.commit()