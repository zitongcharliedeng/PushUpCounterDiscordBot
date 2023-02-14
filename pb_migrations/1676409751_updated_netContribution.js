migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("io58nniitequ5oc")

  // remove
  collection.schema.removeField("hvlgro9h")

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("io58nniitequ5oc")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "hvlgro9h",
    "name": "pushupsRelational",
    "type": "relation",
    "required": false,
    "unique": false,
    "options": {
      "collectionId": "zzio540hdaviyif",
      "cascadeDelete": false,
      "maxSelect": null,
      "displayFields": [
        "pushups"
      ]
    }
  }))

  return dao.saveCollection(collection)
})
