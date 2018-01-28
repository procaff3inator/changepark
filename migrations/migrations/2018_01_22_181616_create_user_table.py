from orator.migrations import Migration


class CreateUserTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cp_users') as table:
            table.increments('id')
            table.string('username')
            table.string('password')
            table.integer('enabled')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cp_users')
