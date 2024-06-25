from graphene import Int, relay


class Connection(relay.Connection):
    total_items = Int()

    class Meta:
        abstract = True

    def resolve_total_items(self, info):
        # TODO: should return as follows -> hasattr(self, "length")
        return len(self.edges)
