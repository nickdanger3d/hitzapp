"""empty message

Revision ID: 4144f33765c7
Revises: None
Create Date: 2015-06-27 19:04:31.662485

"""

# revision identifiers, used by Alembic.
revision = '4144f33765c7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hitters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('overallrating', sa.PickleType(), nullable=True),
    sa.Column('rating', sa.PickleType(), nullable=True),
    sa.Column('lastGamePlayed', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('teamrating', sa.PickleType(), nullable=True),
    sa.Column('overallteamrating', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hometeam_id', sa.Integer(), nullable=True),
    sa.Column('awayteam_id', sa.Integer(), nullable=True),
    sa.Column('winner_id', sa.Integer(), nullable=True),
    sa.Column('awaypoints', sa.Integer(), nullable=True),
    sa.Column('homepoints', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('event', sa.String(), nullable=True),
    sa.Column('gameNumber', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['awayteam_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['hometeam_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hitter_team',
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.Column('hitter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hitter_id'], ['hitters.id'], ),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hitter_team')
    op.drop_table('games')
    op.drop_table('teams')
    op.drop_table('hitters')
    ### end Alembic commands ###
