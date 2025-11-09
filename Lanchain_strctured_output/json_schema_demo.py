{
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": { "type": "string" },
      "description": "A list of the main themes discussed in the review."
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review."
    },
    "sentiment": {
      "type": "string",
      "description": "The overall sentiment of the review, e.g., positive, negative, or neutral."
    },
    "pros": {
      "type": ["array", "null"],
      "items": { "type": "string" },
      "description": "A list of positive aspects mentioned in the review."
    },
    "cons": {
      "type": ["array", "null"],
      "items": { "type": "string" },
      "description": "A list of negative aspects mentioned in the review."
    }
  },
  "required": ["key_themes", "summary", "sentiment", "pros", "cons"]
}
