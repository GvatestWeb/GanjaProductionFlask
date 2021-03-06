"""empty message

Revision ID: d67235eb18eb
Revises: 
Create Date: 2021-03-21 17:19:02.089149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd67235eb18eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('surname', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mails_email'), 'mails', ['email'], unique=True)
    op.create_index(op.f('ix_mails_message'), 'mails', ['message'], unique=False)
    op.create_index(op.f('ix_mails_name'), 'mails', ['name'], unique=False)
    op.create_index(op.f('ix_mails_surname'), 'mails', ['surname'], unique=False)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('photo_path', sa.String(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_photo_path'), 'posts', ['photo_path'], unique=False)
    op.create_index(op.f('ix_posts_text'), 'posts', ['text'], unique=False)
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('review', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reviews_email'), 'reviews', ['email'], unique=False)
    op.create_index(op.f('ix_reviews_name'), 'reviews', ['name'], unique=False)
    op.create_index(op.f('ix_reviews_review'), 'reviews', ['review'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reviews_review'), table_name='reviews')
    op.drop_index(op.f('ix_reviews_name'), table_name='reviews')
    op.drop_index(op.f('ix_reviews_email'), table_name='reviews')
    op.drop_table('reviews')
    op.drop_index(op.f('ix_posts_text'), table_name='posts')
    op.drop_index(op.f('ix_posts_photo_path'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_mails_surname'), table_name='mails')
    op.drop_index(op.f('ix_mails_name'), table_name='mails')
    op.drop_index(op.f('ix_mails_message'), table_name='mails')
    op.drop_index(op.f('ix_mails_email'), table_name='mails')
    op.drop_table('mails')
    # ### end Alembic commands ###
