import dotenv
from src.models.classes.gtzan_model import GtzanModel
from src.models.classes.mfcc_model import MfccModel

dotenv.load_dotenv(override=True)

# gtza_trainer = GtzanModel()
# gtza_trainer.train()

mfcc_trainer = MfccModel()
mfcc_trainer.train()

