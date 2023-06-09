"""Initial migration

Revision ID: 0bab89d16a5c
Revises: 
Create Date: 2023-03-25 20:01:29.356632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bab89d16a5c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('symptom',
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('diagnostic', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('business_symptom_m2m',
    sa.Column('business_id', sa.Integer(), nullable=False),
    sa.Column('symptom_code', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['business_id'], ['business.id'], ),
    sa.ForeignKeyConstraint(['symptom_code'], ['symptom.code'], ),
    sa.PrimaryKeyConstraint('business_id', 'symptom_code')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('business_symptom_m2m')
    op.drop_table('symptom')
    op.drop_table('business')
    # ### end Alembic commands ###
