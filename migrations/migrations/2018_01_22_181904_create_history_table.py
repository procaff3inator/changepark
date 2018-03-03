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
            table.string('address_in')
            table.string('address_out')
            table.string('extraid').nullable()
            # table.string('refund_address')
            # table.string('refund_extraid')
            table.string('transaction_id')
            table.string('exchange_status')
            table.small_integer('sync').default(0)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cp_history')
