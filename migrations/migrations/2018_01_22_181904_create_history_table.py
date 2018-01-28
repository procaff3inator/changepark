from orator.migrations import Migration


class CreateHistoryTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cp_history') as table:
            table.increments('id')
            table.integer('user_id')
            table.string('from_curr')
            table.string('to_curr')
            table.string('amount')
            table.string('address')
            table.string('extraid')
            table.string('refund_address')
            table.string('refund_extraid')
            table.string('transaction_id')
            table.string('exchange_status')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cp_history')
