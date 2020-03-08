# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, Workflow
from trytond.pool import PoolMeta


class ShipmentOut(metaclass=PoolMeta):
    __name__ = 'stock.shipment.out'

    def send_shipment_alert(self):
        """Alert user about shipment status.
        """
        # XXX: Not implemented yet
        return

    @classmethod
    @ModelView.button
    @Workflow.transition('done')
    def done(cls, shipments):
        """Mark shipment done and send an alert to user.
        """
        super(ShipmentOut, cls).done(shipments)

        for shipment in shipments:
            shipment.send_shipment_alert()
