import json


def json_to_xml(json_path, output='bible.xml'):
    """
        Loads json bible and ouput in an xml format
    """
    json_bible = json.load(open(json_path))
    with open(output, 'w') as xml_bible:
        xml_bible.write('<bible>')
        for book in json_bible.get('BIBLEBOOK'):
            book_name = book.get('book_name')
            book_no = book.get('book_number')
            xml_bible.write(f'<{book_name} n={book_no}>')
            chapters = book.get('CHAPTER')

            if isinstance(chapters, dict):
                chapters = [chapters]

            for chapter in chapters:
                chapter_no = chapter.get('chapter_number')
                xml_bible.write(f'<{chapter_no}>')

                for verse in chapter.get('VERSES') or []:
                    verse_no = verse.get('verse_number')
                    verse_text = verse.get('verse_text')
                    xml_bible.write(f'<v n={verse_no}>{verse_text}</v>')

            xml_bible.write(f'</{chapter_no}>')
        xml_bible.write(f'</{book_name}>')


json_path = [
    ('json/full_version/swahili-bible-edition.json', 'xml/full-version.xml'),
    ('json/split_version/agano-jipya-edition.json', 'xml/agano-jipya-edition.xml'),
    ('json/split_version/agano-kale-edition.json', 'xml/agano-kale-edition.xml')
]


for bible_path, out_path in json_path:
    json_to_xml(bible_path, out_path)


print('XML version of bibles generated successfully')
