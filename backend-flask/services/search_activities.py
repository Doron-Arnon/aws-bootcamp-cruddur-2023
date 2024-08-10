from datetime import datetime, timedelta, timezone
class SearchActivities:
  def run(search_term):
    model = {
      'errors': None,
      'data': None
    }

    now = datetime.now(timezone.utc).astimezone()

    if search_term == None or len(search_term) < 1:
      model['errors'] = ['search_term_blank']
    else:
      results = [{            
        'uuid': '68e29e44-9f17-4297-914e-49f0cfcfa152',
        'handle':  'cruddur_yes_name',
        'message': 'Cloud is fun!',
        'created_at': now.isoformat()
      }]
      model['data'] = results
    return model