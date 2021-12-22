from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
class ImportExportUtility:
    def import_file(self, *args, **kwargs):
        if "constr" in kwargs.keys():
            self.constr = kwargs.get("constr")
        if "table_name" in kwargs.keys():
            self.table_name = kwargs.get("table_name")
        if "excel_sheet" in kwargs.keys():
            self.excel_sheet = kwargs.get("excel_sheet")
        Base = automap_base()
        engine = create_engine(self.constr)
        Base.prepare(engine, reflect=True)
        session = Session(engine)
        try:
            self.table=Base.metadata.tables[self.table_name]
        except KeyError:
            self.table=False
        try:
            if not self.table:
                return "table not found"
        except TypeError:
            dfcols=self.excel_sheet.columns.tolist()
            se=dfcols
            se.remove("delete")
            sqlcols=[column.key for column in self.table.columns]
            print(se,sqlcols)
            if se==sqlcols:
                for i,r in self.excel_sheet.iterrows():
                    if not r['delete']:
                        session.query(self.table).filter_by(AlbumId=r['AlbumId'])
                        able=Base.classes
                        ablee=getattr(able,self.table.__str__())
                        if session.query(ablee).filter_by(AlbumId=r['AlbumId']).first() is not None:
                            ds=r.to_dict()
                            del ds['delete']
                            upd=session.query(ablee).filter_by(AlbumId=r['AlbumId']).first()
                            for k,v in ds.items():
                                upd.__setattr__(k,v)
                            session.commit()
                        else:
                            iss=r.to_dict()
                            del iss['delete']
                            able=Base.classes
                            ablee=getattr(able,self.table.__str__())
                            ablew=ablee(**iss)
                            session.add(ablew)
                            session.commit()
                    else:
                        session.query(self.table).filter_by(AlbumId=r['AlbumId']).delete(synchronize_session='evaluate')
                        session.commit()
                return "data imported sucessfully"
            else:
                return "columes does not match"
        return "ok"
    def export(self,**kwargs):
        pass

        
        