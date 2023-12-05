//xxi
program HelloWorld;

uses
 Sysutils, Classes, StrUtils, Types;

function read_file(): TStringList;
const
    FILENAME = 'input';
var
    input: TextFile;
    input_string: string;
    Result: TStringList;
begin
    Result := TStringList.Create;
    Assign(input, FILENAME);
    reset(input);
    while not eof(input) do
    begin
        readln(input, input_string);
        Result.Add(input_string);
    end;
    read_file := Result;
end;


function evaluate1(input: TStringList): integer;
var
    valid: Boolean;
    str: string;
    i: integer;
    Result: integer;
    split: TStringDynArray;
    handfuls: TStringDynArray;
    handful: string;
    marbels: TStringDynArray;
    marbel: string;
    linenumber: integer;
    number: string;
    color: string;
    
begin
    Result := 0;
    for i := 0 to input.Count - 1 do
    begin

        str := input[i];
        split := SplitString(str, ':');
        linenumber := StrToInt(SplitString(split[0],' ')[1] );
        
        handfuls := SplitString(split[1],';');
        valid := True;
        for handful in handfuls do
        begin 
            marbels := SplitString(handful,',');
            for marbel in marbels do
            begin 
                number := SplitString(marbel,' ')[1];
                color := SplitString(marbel,' ')[2];
                if color = 'red' then
                    if StrToInt(number) > 12 then
                        valid := false;
                if color = 'green' then
                    if StrToInt(number) > 13 then
                        valid := false;
                if color = 'blue' then
                    if StrToInt(number) > 14 then
                        valid := false;
            end;
        end;
        if valid = true then
            Result := Result + linenumber;
    end; 


    evaluate1 := Result;
end;

function evaluate2(input: TStringList): Longint;
var
    str: string;
    i: integer;
    Result: Longint;
    split: TStringDynArray;
    handfuls: TStringDynArray;
    handful: string;
    marbels: TStringDynArray;
    marbel: string;
    reds: integer;
    blues: integer;
    greens: integer;
    power: integer;
    number: string;
    color: string;
begin
    Result := 0;
    for i := 0 to input.Count - 1 do
    begin

        str := input[i];
        split := SplitString(str, ':');
        handfuls := SplitString(split[1],';');
        blues := 1;
        reds := 1;
        greens := 1;
        for handful in handfuls do
        begin 
            marbels := SplitString(handful,',');
            for marbel in marbels do
            begin 
                number := SplitString(marbel,' ')[1];
                color := SplitString(marbel,' ')[2];
                if color = 'red' then
                begin
                    if StrToInt(number) > reds then 
                    begin
                        reds := StrToInt(number);
                    end;
                end;
                if color = 'green' then
                begin
                    begin 
                    if StrToInt(number) > greens then
                        greens := StrToInt(number);
                    end;
                end;
                if color = 'blue' then
                begin
                    begin
                        if StrToInt(number) > blues then
                            blues := StrToInt(number);
                    end;
                end;
            end;
        end;
        power := (reds*blues)*greens;
        Result := Result + power;
    end; 

    evaluate2 := Result;
end;

var
    data: TStringList;
begin
    data:= read_file();
    writeln('Part 1: ', evaluate1(data));
    writeln('Part 2: ', evaluate2(data));
end.

