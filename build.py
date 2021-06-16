from build_docs import Documentation

Docs = Documentation()
print(Docs.templates, Docs.sources)
Docs.generate().save(split_by=None)
print(Docs.template_content)
# breakpoint()
