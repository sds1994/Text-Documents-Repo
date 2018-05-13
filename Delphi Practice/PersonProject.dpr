program PersonProject;

uses
  Vcl.Forms,
  PersonUnit in 'PersonUnit.pas' {PersonForm};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TPersonForm, PersonForm);
  Application.Run;
end.
