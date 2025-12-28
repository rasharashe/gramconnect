from core.models import Squad



def create_squads(user):
    squads = [
        {'short_name': 'rac', 'name': 'RAC'},
        {'short_name': 'plr', 'name': 'Palora'},
        {'short_name': 'kkd', 'name': 'Kaithakkund'},
        {'short_name': 'cc', 'name': 'CC Peedika'},
        {'short_name': 'smk', 'name': 'S Mukk'},
        {'short_name': 'knt', 'name': 'Kannoth'},
        {'short_name': 'knd', 'name': 'Kuningad'},
    ]
    for squad_data in squads:
        Squad.objects.create(
            short_name=squad_data['short_name'],
            name=squad_data['name'],
            created_by=user
        )
    return


class GetSidebarContext:
    def __init__(self, request):
        self.request = request

    def get_context(self):
        squads = Squad.objects.all()
        return {
            'squads': squads,
        }