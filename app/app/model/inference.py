import io

import torch
import torch.nn as nn
from torchvision import transforms, models

from PIL import Image
from pathlib import Path


transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

checkpoint = Path('app/model/checkpoint.pt')
model = models.vgg16(pretrained=True)

model.features = nn.Sequential(*list(model.features.children())[:-3])
model.classifier = nn.Sequential(*[nn.Linear(25088, 4096), nn.ReLU(inplace=True),
                                   nn.Dropout(p=.5), nn.Linear(4096, 3)])
	
for param in model.features.parameters():
	param.requires_grad = False
	
model.load_state_dict(torch.load(checkpoint, map_location='cpu'))

label_title = ["melanoma", "nevus", "seborrheic_keratosis"]

def label(bytes):
	tensor = transform(Image.open(io.BytesIO(bytes))).unsqueeze(0)
	output = model(tensor)
	print(output)
	pred = output.data.max(1, keepdim=True)[1]

	return label_title[pred.item()]