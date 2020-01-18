import io

import torch
from torchvision import transforms, models

from PIL import Image
from pathlib import Path


transform = transforms.Compose([
    	transforms.CenterCrop(224),
    	transforms.ToTensor(),
    	transforms.Normalize([.5,.5,.5], [.5,.5,.5])
    ])

checkpoint = Path('app/model/skin_cancer_model.pt')
model = models.densenet201(pretrained=True)
	
for param in model.features.parameters():
	param.requires_grad = False
    
in_feat = model.classifier.in_features
model.classifier = torch.nn.Linear(in_feat, 3)
	
model.load_state_dict(torch.load(checkpoint, map_location='cpu'))

label_title = ["melanoma", "nevus", "seborrheic_keratosis"]

def label(bytes):
	tensor = transform(Image.open(io.BytesIO(bytes))).unsqueeze(0)
	output = model(tensor)
	pred = output.data.max(1, keepdim=True)[1]

	return label_title[pred.item()]