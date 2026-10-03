import React, {useState} from 'react';
import axios from 'axios';

const API='http://localhost:8000/api';

export default function App(){
  const [req,setReq]=useState('Test a login page with valid and invalid credentials');
  const [url,setUrl]=useState('https://example.com');
  const [cases,setCases]=useState([]);
  const [result,setResult]=useState(null);
  const [loading,setLoading]=useState(false);

  async function generate(){
    setLoading(true);
    try{ const r=await axios.post(API+'/test-cases/generate',{requirement:req}); setCases(r.data.test_cases); }
    catch(e){alert(e.response?.data?.detail||e.message)} finally{setLoading(false)}
  }
  async function run(){
    setLoading(true);
    try{ const r=await axios.post(API+'/tests/run',{url}); setResult(r.data); }
    catch(e){alert(e.response?.data?.detail||e.message)} finally{setLoading(false)}
  }
  return <div className="app">
    <aside><div className="logo">⚡ TestPilot <span>AI</span></div>
      <nav><div className="active">Dashboard</div><div>Test Cases</div><div>Test Runs</div><div>Bug Analyzer</div></nav>
      <div className="agent">🤖 <b>AI Agent</b><small>Ready to test</small></div>
    </aside>
    <main>
      <header><div><h1>AI Test Automation</h1><p>Generate, execute and analyze software tests with an AI agent.</p></div><button onClick={generate}>＋ New AI Test</button></header>
      <section className="stats"><Card n={cases.length||24} t="Test Cases"/><Card n={result?.status==='passed'?1:8} t="Passed"/><Card n={result?.status==='failed'?1:2} t="Failed"/><Card n="96%" t="Coverage"/></section>
      <section className="grid">
        <div className="panel wide"><h2>Requirement → AI Test Cases</h2><textarea value={req} onChange={e=>setReq(e.target.value)}/><button className="primary" onClick={generate} disabled={loading}>{loading?'Generating…':'Generate Test Cases'}</button>
        <div className="cases">{cases.map((c,i)=><div className="case" key={i}><b>TC-{String(i+1).padStart(3,'0')} · {c.title}</b><p>{c.steps.join(' → ')}</p><small>Expected: {c.expected}</small></div>)}</div></div>
        <div className="panel"><h2>Browser Smoke Test</h2><input value={url} onChange={e=>setUrl(e.target.value)}/><button className="primary" onClick={run} disabled={loading}>▶ Run Test</button>{result&&<div className={'result '+result.status}><strong>{result.status.toUpperCase()}</strong><pre>{JSON.stringify(result,null,2)}</pre></div>}</div>
      </section>
    </main>
  </div>
}
function Card({n,t}){return <div className="stat"><strong>{n}</strong><span>{t}</span></div>}
