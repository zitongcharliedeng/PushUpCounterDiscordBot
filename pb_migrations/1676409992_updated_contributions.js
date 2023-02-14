migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("zzio540hdaviyif")

  // remove
  collection.schema.removeField("d8xfdygd")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("zzio540hdaviyif")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "d8xfdygd",
    "name": "time",
    "type": "date",
    "required": false,
    "unique": false,
    "options": {
      "min": "",
      "max": ""
    }
  }))

  return dao.saveCollection(collection)
})
