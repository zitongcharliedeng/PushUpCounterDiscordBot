migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("u6y1r381qcg6kc6")

  collection.name = "contributions"

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("u6y1r381qcg6kc6")

  collection.name = "contributionsd"

  return dao.saveCollection(collection)
})
