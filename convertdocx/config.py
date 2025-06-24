# config.py

# Global document styles
DOCX_STYLE = {
    "font_name": "Calibri",
    "font_size": 11,
    "line_spacing": 1.15,
    "heading_color": "000000",  # H1 - Black
    "body_text_color": "000000",  # Standard body text
    "meta_text_color": "666666",  # Gray for metadata/frontmatter
    "margin_inches": 1.0,

    "heading_styles": {
        "Heading 1": {"size": 18, "bold": True, "color": "000000"},  # Black
        "Heading 2": {"size": 14, "bold": True, "color": "8B0000"},  # Brick Red
        "Heading 3": {"size": 12, "bold": True, "color": "000080"},  # Navy Blue
    },

    "bullet_style": {
        "symbol": "•",
        "font_size": 11,
    }
}
