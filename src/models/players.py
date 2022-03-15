from configs.database import database

class Players:
  def __init__(self):
    self.database = database

  def create(self, body):
    created_contact = self.database.contacts.insert_one(body)

    if not created_contact.inserted_id:
      raise 'Erro ao criar um novo jogador, tente novamente.'

  def update(self, id, body):
    updated_contact = self.database.contacts.update_one(
      { '_id': id },
      { '$set': body }
    )

    if updated_contact.modified_count < 1:
      raise 'Erro ao atualizar o contato, tente novamente.'

  def remove(self, id):
    removed_contact = self.database.contacts.delete_one({'_id': id })

    if removed_contact.deleted_count < 1:
      raise 'Erro ao deletar o contato, tente novamente.'

  def get_ranking(self, params = None):
    query = []

    if params:
      if 'name' in params:
        params['name'] = { '$regex': params['name'] }
        
      if 'phone' in params:
        params['phone'] = { '$regex': params['phone'] }
      query.append({ "$match": params })

    contacts = self.database.contacts.aggregate(query)

    return list(contacts)