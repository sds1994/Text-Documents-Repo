unit PersonUnit;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Data.DB, Data.Win.ADODB, Vcl.StdCtrls,
  Vcl.Mask, Vcl.DBCtrls, Vcl.Grids, Vcl.DBGrids;

type
  TPersonForm = class(TForm)
    DBGrid1: TDBGrid;
    DBEdit1: TDBEdit;
    DBEdit2: TDBEdit;
    DataSource1: TDataSource;
    ADOConnection1: TADOConnection;
    SelPersonProc: TADOStoredProc;
    procedure FormCreate(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  PersonForm: TPersonForm;

implementation

{$R *.dfm}

procedure TPersonForm.FormCreate(Sender: TObject);
begin
  SelPersonProc.ExecProc;
end;

end.
