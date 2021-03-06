"""Initial Setup

Revision ID: 52421aa80a74
Revises: 
Create Date: 2020-08-11 10:41:24.676575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52421aa80a74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    genres_table = op.create_table('genres',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(genres_table, [
        {'id': 1, 'name': 'Alternative'},
        {'id': 2, 'name': 'Blues'},
        {'id': 3, 'name': 'Classical'},
        {'id': 4, 'name': 'Country'},
        {'id': 5, 'name': 'Electronic'},
        {'id': 6, 'name': 'Folk'},
        {'id': 7, 'name': 'Funk'},
        {'id': 8, 'name': 'Hip-Hop'},
        {'id': 9, 'name': 'Heavy Metal'},
        {'id': 10, 'name': 'Instrumental'},
        {'id': 11, 'name': 'Jazz'},
        {'id': 12, 'name': 'Musical Theatre'},
        {'id': 13, 'name': 'Pop'},
        {'id': 14, 'name': 'Punk'},
        {'id': 15, 'name': 'R&B'},
        {'id': 16, 'name': 'Reggae'},
        {'id': 17, 'name': 'Rock n Roll'},
        {'id': 18, 'name': 'Soul'},
        {'id': 19, 'name': 'Swing'},
        {'id': 20, 'name': 'Other'},
    ])

    states_table = op.create_table('states',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(states_table, [
        {'id': 1, 'name': 'AL'},
        {'id': 2, 'name': 'AK'},
        {'id': 3, 'name': 'AZ'},
        {'id': 4, 'name': 'AR'},
        {'id': 5, 'name': 'CA'},
        {'id': 6, 'name': 'CO'},
        {'id': 7, 'name': 'CT'},
        {'id': 8, 'name': 'DE'},
        {'id': 9, 'name': 'DC'},
        {'id': 10, 'name': 'FL'},
        {'id': 11, 'name': 'GA'},
        {'id': 12, 'name': 'HI'},
        {'id': 13, 'name': 'ID'},
        {'id': 14, 'name': 'IL'},
        {'id': 15, 'name': 'IN'},
        {'id': 16, 'name': 'IA'},
        {'id': 17, 'name': 'KS'},
        {'id': 18, 'name': 'KY'},
        {'id': 19, 'name': 'LA'},
        {'id': 20, 'name': 'ME'},
        {'id': 21, 'name': 'MT'},
        {'id': 22, 'name': 'NE'},
        {'id': 23, 'name': 'NV'},
        {'id': 24, 'name': 'NH'},
        {'id': 25, 'name': 'NJ'},
        {'id': 26, 'name': 'NM'},
        {'id': 27, 'name': 'NY'},
        {'id': 28, 'name': 'NC'},
        {'id': 29, 'name': 'ND'},
        {'id': 30, 'name': 'OH'},
        {'id': 31, 'name': 'OK'},
        {'id': 32, 'name': 'OR'},
        {'id': 33, 'name': 'MD'},
        {'id': 34, 'name': 'MA'},
        {'id': 35, 'name': 'MI'},
        {'id': 36, 'name': 'MN'},
        {'id': 37, 'name': 'MS'},
        {'id': 38, 'name': 'MO'},
        {'id': 39, 'name': 'PA'},
        {'id': 40, 'name': 'RI'},
        {'id': 41, 'name': 'SC'},
        {'id': 42, 'name': 'SD'},
        {'id': 43, 'name': 'TN'},
        {'id': 44, 'name': 'TX'},
        {'id': 45, 'name': 'UT'},
        {'id': 46, 'name': 'VT'},
        {'id': 47, 'name': 'VA'},
        {'id': 48, 'name': 'WA'},
        {'id': 49, 'name': 'WV'},
        {'id': 50, 'name': 'WI'},
        {'id': 51, 'name': 'WY'},
    ])

    op.create_table('artists',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('city', sa.String(length=120), nullable=False),
        sa.Column('phone', sa.String(length=120), nullable=False),
        sa.Column('image_link', sa.String(length=500), nullable=True),
        sa.Column('facebook_link', sa.String(length=120), nullable=True),
        sa.Column('website', sa.String(length=120), nullable=True),
        sa.Column('seeking_venue', sa.Boolean(), nullable=True),
        sa.Column('seeking_description', sa.String(), nullable=True),
        sa.Column('available_from', sa.DateTime(timezone=True), nullable=True),
        sa.Column('available_to', sa.DateTime(timezone=True), nullable=True),
        sa.Column('state_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('venues',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('city', sa.String(length=120), nullable=False),
        sa.Column('address', sa.String(length=120), nullable=False),
        sa.Column('phone', sa.String(length=120), nullable=False),
        sa.Column('image_link', sa.String(length=500), nullable=True),
        sa.Column('facebook_link', sa.String(length=120), nullable=True),
        sa.Column('website', sa.String(length=120), nullable=True),
        sa.Column('seeking_talent', sa.Boolean(), nullable=True),
        sa.Column('seeking_description', sa.String(), nullable=True),
        sa.Column('state_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['state_id'], ['states.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('artist_genres',
        sa.Column('artist_id', sa.Integer(), nullable=False),
        sa.Column('genre_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
        sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
        sa.PrimaryKeyConstraint('artist_id', 'genre_id')
    )

    op.create_table('shows',
        sa.Column('venue_id', sa.Integer(), nullable=False),
        sa.Column('artist_id', sa.Integer(), nullable=False),
        sa.Column('start_time', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
        sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
        sa.PrimaryKeyConstraint('venue_id', 'artist_id', 'start_time')
    )

    op.create_table('venue_genres',
        sa.Column('venue_id', sa.Integer(), nullable=False),
        sa.Column('genre_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
        sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
        sa.PrimaryKeyConstraint('venue_id', 'genre_id')
    )


def downgrade():
    op.drop_table('venue_genres')
    op.drop_table('shows')
    op.drop_table('artist_genres')
    op.drop_table('venues')
    op.drop_table('artists')
    op.drop_table('states')
    op.drop_table('genres')
