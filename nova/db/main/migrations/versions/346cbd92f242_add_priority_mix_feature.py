# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Add priority mix feature

Revision ID: 346cbd92f242
Revises: 16f1fbcab42b
Create Date: 2022-05-23 09:09:30.280865
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '346cbd92f242'
down_revision = '16f1fbcab42b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('instances', sa.Column('priority', sa.String(255)))
