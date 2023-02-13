migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("zzio540hdaviyif")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "gyg291zc",
    "name": "userId",
    "type": "text",
    "required": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("zzio540hdaviyif")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "gyg291zc",
    "name": "userId",
    "type": "text",
    "required": false,
    "unique": true,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  return dao.saveCollection(collection)
})
