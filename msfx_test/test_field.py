import msfx.db.table
from msfx.db.field import Field
from msfx.db.types import Types
from msfx.db.table import Table

f_carticle = Field()
f_carticle.set_name("CARTICLE")
f_carticle.set_type(Types.STRING)
f_carticle.set_length(40)

f_qsales = Field()
f_qsales.set_name("QSALES")
f_qsales.set_type(Types.DECIMAL)
f_qsales.set_length(20)
f_qsales.set_decimals(4)

print(f_carticle)
print(f_qsales)

f_ccomponent = Field(f_carticle)
f_ccomponent.set_name("CCOMPONENT")

t_arts = Table()
t_arts.set_name("COMPONENTS")
f_ccomponent.set_table(t_arts)

print(f_ccomponent)

table = msfx.db.table.Table()

