import uuid

def get_products():
	fake_response = [{
		"sku": uuid.uuid4(),
		"title": "Vanilla icecream",
		"long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur blandit mattis nisl vitae fermentum. Cras eu tincidunt arcu. Etiam vitae urna lectus. Integer placerat bibendum magna sit amet vulputate. Donec venenatis aliquet dignissim. Sed et nisi at tortor venenatis auctor. Duis condimentum faucibus tincidunt. Nunc posuere dolor massa. Nunc vulputate metus ut dolor vulputate aliquam. Phasellus condimentum nec dui id pellentesque. Cras at nisi egestas, interdum erat eu, lacinia felis. Ut id rutrum velit. Ut nulla erat, placerat non mi non, iaculis finibus quam. Sed finibus nisl vitae nulla facilisis laoreet. Suspendisse porttitor lectus ut ultricies tincidunt.",
	"price_euro": 1.5
	},{
        "sku": uuid.uuid4(),
        "title": "Vanilla icecream",
        "long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur blandit mattis nisl vitae fermentum. Cras eu tincidunt arcu. Etiam vitae urna lectus. Integer placerat bibendum magna sit amet vulputate. Donec venenatis aliquet dignissim. Sed et nisi at tortor venenatis auctor. Duis condimentum faucibus tincidunt. Nunc posuere dolor massa. Nunc vulputate metus ut dolor vulputate aliquam. Phasellus condimentum nec dui id pellentesque. Cras at nisi egestas, interdum erat eu, lacinia felis. Ut id rutrum velit. Ut nulla erat, placerat non mi non, iaculis finibus quam. Sed finibus nisl vitae nulla facilisis laoreet. Suspendisse porttitor lectus ut ultricies tincidunt.",
    "price_euro": 1.5
    },{
        "sku": uuid.uuid4(),
        "title": "Vanilla icecream",
        "long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur blandit mattis nisl vitae fermentum. Cras eu tincidunt arcu. Etiam vitae urna lectus. Integer placerat bibendum magna sit amet vulputate. Donec venenatis aliquet dignissim. Sed et nisi at tortor venenatis auctor. Duis condimentum faucibus tincidunt. Nunc posuere dolor massa. Nunc vulputate metus ut dolor vulputate aliquam. Phasellus condimentum nec dui id pellentesque. Cras at nisi egestas, interdum erat eu, lacinia felis. Ut id rutrum velit. Ut nulla erat, placerat non mi non, iaculis finibus quam. Sed finibus nisl vitae nulla facilisis laoreet. Suspendisse porttitor lectus ut ultricies tincidunt.",
    "price_euro": 1.5
    },{
        "sku": uuid.uuid4(),
        "title": "Vanilla icecream",
        "long_description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur blandit mattis nisl vitae fermentum. Cras eu tincidunt arcu. Etiam vitae urna lectus. Integer placerat bibendum magna sit amet vulputate. Donec venenatis aliquet dignissim. Sed et nisi at tortor venenatis auctor. Duis condimentum faucibus tincidunt. Nunc posuere dolor massa. Nunc vulputate metus ut dolor vulputate aliquam. Phasellus condimentum nec dui id pellentesque. Cras at nisi egestas, interdum erat eu, lacinia felis. Ut id rutrum velit. Ut nulla erat, placerat non mi non, iaculis finibus quam. Sed finibus nisl vitae nulla facilisis laoreet. Suspendisse porttitor lectus ut ultricies tincidunt.",
    "price_euro": 1.5
    }]

	return fake_response

def create_product(sku, title, long_description, price_euro):
	''' '''
	print("Ha funcionado");
