n=20
[x,t]=func1(n);
scatter(t,x);
function [signal,timestamp]=func1(n)
    signal=[]
    timestamp=[];
    if n<0
        return 
    end
    
    if n>20
        return
    end
    
    for i=1:n
        temp=(0.9)^i
        signal=[signal temp]
        timestamp=[timestamp i]
        %x[i]=signal
    end
end