"""init

Revision ID: d5dabeb3461c
Revises: e17a5707ad65
Create Date: 2022-04-14 01:57:00.915773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5dabeb3461c'
down_revision = 'e17a5707ad65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schoolyears',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_schoolyears_title'), 'schoolyears', ['title'], unique=True)
    op.create_table('students',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('father_name', sa.String(), nullable=False),
    sa.Column('gfather_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('gender', sa.Boolean(), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('guardian_phone_no', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gradesubjects',
    sa.Column('grade_id', sa.SmallInteger(), nullable=False),
    sa.Column('subject_id', sa.SmallInteger(), nullable=False),
    sa.ForeignKeyConstraint(['grade_id'], ['grades.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
    sa.PrimaryKeyConstraint('grade_id', 'subject_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gradesubjects')
    op.drop_table('students')
    op.drop_index(op.f('ix_schoolyears_title'), table_name='schoolyears')
    op.drop_table('schoolyears')
    # ### end Alembic commands ###