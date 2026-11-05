"""An import does not run the guarded demonstration table."""
import milkrate
print('Imported successfully; one requested payment:', milkrate.payout(10, 3.5, 8.5))
