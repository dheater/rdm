import pytest
from jinja2.ext import Extension

from rdm.util import dynamic_class_loader, extract_module_and_class


def test_dynamic_class_loader():
    extensions = dynamic_class_loader(['rdm.md_extensions.audit_notes.AuditNoteExclusionExtension'])
    assert extensions is not None
    assert len(extensions) == 1
    extension = extensions[0]
    assert issubclass(extension, Extension)


@pytest.mark.parametrize('description, expected_module_name, expected_class_name', [
    ('this.that', 'this', 'that'),
    ('this.that.another', 'this.that', 'another'),
])
def test_extract_module_and_class(description, expected_module_name, expected_class_name):
    actual_module_name, actual_class_name = extract_module_and_class(description)
    assert actual_module_name == expected_module_name
    assert actual_class_name == expected_class_name